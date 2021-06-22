import { Component, OnInit } from '@angular/core';
import { NgbModal } from '@ng-bootstrap/ng-bootstrap';
import { Product } from '../models/product-model';
import { ProductService } from '../services/product.service';
import { AddProductComponent } from './add-product/add-product.component';

@Component({
  selector: 'app-products',
  templateUrl: './products.component.html',
  styleUrls: ['./products.component.css']
})
export class ProductsComponent implements OnInit {

  products: Product[];

  constructor(private productService: ProductService, private modalService: NgbModal) { }

  ngOnInit(): void {
    this.getProducts()
  }

  getProducts() {
    this.productService.get().subscribe(data => {
      this.products = data
    }, err => {
      alert(err)
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
