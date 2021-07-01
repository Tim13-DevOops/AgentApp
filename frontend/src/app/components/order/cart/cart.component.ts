import { Component, OnInit } from '@angular/core';
import { ProductQuantity } from 'src/app/models/product-quantity.model';
import { CartService } from 'src/app/services/cart.service';

@Component({
  selector: 'app-cart',
  templateUrl: './cart.component.html',
  styleUrls: ['./cart.component.css']
})
export class CartComponent implements OnInit {

  cart: ProductQuantity[]

  constructor(private cartService: CartService) { }

  ngOnInit(): void {
    this.cart = this.cartService.getCart()
  }

  removeItem(item: ProductQuantity) {
    let itemIndex = this.cart.indexOf(item)

    if (itemIndex !== -1) {
      this.cart.splice(itemIndex, 1)
      this.cartService.saveCart(this.cart)
    }

  }

  updateItemQuantity(item: ProductQuantity, quantity: number) {
    let itemIndex = this.cart.indexOf(item)
    if (itemIndex !== -1) {
      this.cart[itemIndex].quantity = +quantity
      this.cartService.saveCart(this.cart)
    }

  }

}
