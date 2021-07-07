import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';
import { AuthService } from 'src/app/services/auth.service';
import { ToastService } from 'src/app/services/toast.service';

@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.css']
})
export class LoginComponent implements OnInit {

  credentials = {
    username: "",
    password: "",
  }

  constructor(private toastService: ToastService,
    private authService: AuthService,
    private router: Router) { }

  ngOnInit(): void {
  }

  login() {
    if (!this.credentials.username || !this.credentials.password) {
      this.toastService.show("Please enter usename and password")
    }
    this.authService.login(this.credentials).subscribe((user: any) => {
      this.toastService.show("Welcome");
      this.router.navigateByUrl('/home');
    }, err => {
      this.toastService.show("Invalid credentials.")
    })
  }

}
