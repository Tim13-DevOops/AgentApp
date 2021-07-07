import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { map } from 'rxjs/operators';
import { environment } from 'src/environments/environment';
import jwt_decode from 'jwt-decode';
import { BehaviorSubject, Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class AuthService {

  private _user: BehaviorSubject<any> = new BehaviorSubject(undefined);

  public userObservable = this._user.asObservable();

  constructor(private http: HttpClient) { }

  login(credentials) {
    return this.http.post(`${environment.auth_url}/login`, credentials).pipe(map((token: any) => {
      let user: any = jwt_decode(token);
      user.token = token;
      localStorage.setItem("user", JSON.stringify(user))
      this._user.next(user);
      return user;
    }))
  }

  getUser() {
    return this._user.value;
  }

  logout() {
    this._user.next(null);
    localStorage.removeItem("user");
  }

}
