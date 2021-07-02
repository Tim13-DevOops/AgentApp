import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';
import { map } from 'rxjs/operators';
import { environment } from 'src/environments/environment';
import { Order } from '../models/order.model';

const baseURL = `${environment.api_url}/order`

@Injectable({
  providedIn: 'root'
})
export class OrderService {

  constructor(private http: HttpClient) { }


  postOrder(order: Order): Observable<Order> {
    return this.http.post(baseURL, order).pipe(map((data: any) => {
      return new Order(data);
    }))
  }

}
