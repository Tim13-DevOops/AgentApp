import { Injectable } from '@angular/core';
import { ProductQuantity } from '../models/product-quantity';

@Injectable({
  providedIn: 'root'
})
export class CartService {

  constructor() { }

  
  addToCart(productQuantity: ProductQuantity) {
    let cart = this.getCart()

    let productInCart = false

    for (let pq of cart) {
      if (pq.product.id == productQuantity.product.id) {
        pq.quantity += productQuantity.quantity
        productInCart = true
        break;
      }
    }

    if (!productInCart) {
      cart.push(productQuantity)
    }

    this.saveCart(cart)

  }

  getCart(): ProductQuantity[] {
    let cartString = localStorage.getItem("cart")
    if (cartString) {
      return JSON.parse(cartString)
    } else {
      return []
    }
  }

  saveCart(cart: ProductQuantity[]): void {
    let cartString = JSON.stringify(cart)
    localStorage.setItem("cart", cartString)
  }
}
