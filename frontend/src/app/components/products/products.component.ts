import { Component, OnInit } from '@angular/core';
import { NgbModal } from '@ng-bootstrap/ng-bootstrap';
import { Product } from '../../models/product.model';
import { ProductService } from '../../services/product.service';
import { AddProductComponent } from './add-product/add-product.component';
import { faPlus } from '@fortawesome/free-solid-svg-icons'
import { AuthService } from 'src/app/services/auth.service';
import { ToastService } from 'src/app/services/toast.service';

@Component({
  selector: 'app-products',
  templateUrl: './products.component.html',
  styleUrls: ['./products.component.css']
})
export class ProductsComponent implements OnInit {

  products: Product[];

  user: any = undefined;

  iconAdd = faPlus;

  constructor(private productService: ProductService, private modalService: NgbModal, private authService: AuthService, private toastService: ToastService) { }

  ngOnInit(): void {
    this.getProducts()
    this.user = this.authService.getUser();

  }

  getProducts() {
    this.productService.get().subscribe(data => {
      this.products = data
    }, err => {
      this.toastService.show(`${err.code} ${err.message}`, { classname: 'bg-danger text-light', delay: 5000 })
    })
  }

  openAddDialog() {
    const modalRef = this.modalService.open(AddProductComponent);
    modalRef.closed.subscribe(() => {
      this.getProducts()
    })
  }

  handleProductsChanged() {
    this.getProducts()
  }
}
