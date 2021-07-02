import { Component, OnInit } from '@angular/core';
import { Order } from '../../models/order.model';
import { CartService } from '../../services/cart.service';
import { OrderService } from '../../services/order.service';
import { ToastService } from '../../services/toast.service';

@Component({
  selector: 'app-order',
  templateUrl: './order.component.html',
  styleUrls: ['./order.component.css']
})
export class OrderComponent implements OnInit {

  order: Order = new Order();

  constructor(private orderService: OrderService,
    private cartService: CartService,
    private toastService: ToastService) { }

  ngOnInit(): void {
  }

  makeOrder() {
    let cart = this.cartService.getCart()
    console.log(cart);
    console.log(this.cartService.mapCartToOrder(cart));
    this.order.products = this.cartService.mapCartToOrder(cart);

    this.orderService.postOrder(this.order).subscribe((result: Order) => {
      this.toastService.show("Order sent", { classnmae: 'bg-success text-light', delay: 5000 })
      console.log(result)
    })
  }


}
