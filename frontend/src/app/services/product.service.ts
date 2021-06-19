import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';

import { map } from 'rxjs/operators';

const baseURL = 'http://localhost:5000/product'

@Injectable({
  providedIn: 'root'
})
export class ProductService {

  constructor(private http: HttpClient) { }

  get(): Observable<any> {
    return this.http.get(baseURL).pipe(map(result => {
      return result
    }))
  }
}
