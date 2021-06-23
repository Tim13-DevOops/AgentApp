import { Component, OnInit } from '@angular/core';
import { CartService } from '../services/cart.service';
import { OrderService } from '../services/order.service';

@Component({
  selector: 'app-order',
  templateUrl: './order.component.html',
  styleUrls: ['./order.component.css']
})
export class OrderComponent implements OnInit {

  firstName = "";
  lastName = "";

  constructor(private orderService: OrderService,
              private cartService: CartService) { }

  ngOnInit(): void {
  }

  makeOrder() {
    let cart = this.cartService.getCart()
    console.log(cart)
  }


}
