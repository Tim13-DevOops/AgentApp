import { Component, OnInit } from '@angular/core';
import { ActivatedRoute, Router } from '@angular/router';
import { Product } from 'src/app/models/product.model';
import { ProductQuantity } from 'src/app/models/product-quantity.model';
import { CartService } from 'src/app/services/cart.service';
import { ProductService } from 'src/app/services/product.service';
import { environment } from 'src/environments/environment';
import { ToastService } from 'src/app/services/toast.service';

@Component({
  selector: 'app-product-page',
  templateUrl: './product-page.component.html',
  styleUrls: ['./product-page.component.css']
})
export class ProductPageComponent implements OnInit {

  product_id: number
  product: Product

  images_url = environment.images_url;

  amount = 0

  constructor(private route: ActivatedRoute,
    private service: ProductService,
    private cartService: CartService,
    private toastService: ToastService) { }

  ngOnInit(): void {
    this.route.params.subscribe(routeParams => {
      this.product_id = routeParams['product_id'];
      this.getProduct();
    })
  }

  getProduct(): void {
    this.service.getOne(this.product_id).subscribe(product => {
      this.product = product;
    }, err => {
      this.toastService.show(`${err.code} ${err.message}`, { classname: 'bg-danger text-light', delay: 5000 })
    })
  }

  addToCart() {
    if (this.amount <= 0) {
      this.toastService.show("Amount must be greater than 0.", { classnmae: 'bg-danger text-light', delay: 5000 })
      return
    }

    this.cartService.addToCart({
      product: new Product(this.product),
      quantity: this.amount
    })

    this.amount = 0

  }

}
