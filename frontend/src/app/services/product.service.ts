import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';
import { Product } from '../models/product.model';

import { map } from 'rxjs/operators';
import { environment } from 'src/environments/environment';

const baseURL = `${environment.api_url}/product`

@Injectable({
  providedIn: 'root'
})
export class ProductService {

  constructor(private http: HttpClient) { }

  get(): Observable<Product[]> {
    return this.http.get(baseURL).pipe(map((result: any) => {
      return result.map(item => new Product(item))
    }))
  }

  getOne(id: number): Observable<Product> {
    return this.http.get(`${baseURL}/${id}`).pipe(map((result: any) => {
      return new Product(result)
    }))
  }

  post(product: Product): Observable<Product> {
    return this.http.post(baseURL, product).pipe(map((result: any) => {
      return new Product(result)
    }))
  }

  put(product: Product): Observable<Product> {
    return this.http.put(baseURL, product).pipe(map((result: any) => {
      return new Product(result)
    }))
  }


  delete(id: number): Observable<Product> {
    return this.http.delete(`${baseURL}/${id}`).pipe(map((result: any) => {
      return new Product(result)
    }))
  }
}
