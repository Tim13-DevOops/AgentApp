import { Component, EventEmitter, Input, OnInit, Output } from '@angular/core';
import { NgbModal } from '@ng-bootstrap/ng-bootstrap';
import { Product } from 'src/app/models/product.model';
import { AuthService } from 'src/app/services/auth.service';
import { ProductService } from 'src/app/services/product.service';
import { ToastService } from 'src/app/services/toast.service';
import { environment } from 'src/environments/environment';
import { UpdateProductComponent } from '../update-product/update-product.component';

@Component({
  selector: 'app-product',
  templateUrl: './product.component.html',
  styleUrls: ['./product.component.css']
})
export class ProductComponent implements OnInit {

  @Input()
  product: Product

  user: any = undefined;

  images_url = environment.images_url;

  @Output()
  productsChanged = new EventEmitter<boolean>()

  constructor(private modalService: NgbModal, private productService: ProductService,
    private authService: AuthService, private toastService: ToastService) { }

  ngOnInit(): void {
    this.user = this.authService.getUser()
  }

  openEditDialog() {
    let modalRef = this.modalService.open(UpdateProductComponent)
    modalRef.componentInstance.product = new Product(this.product)
    modalRef.closed.subscribe(() => {
      this.productsChanged.emit(true)
    })
  }

  deleteProduct() {
    this.productService.delete(this.product.id).subscribe(result => {
      this.productsChanged.emit(true)
    }, err => {
      this.toastService.show(`${err.code} ${err.message}`, { classname: 'bg-danger text-light', delay: 5000 })
    })
  }

}
