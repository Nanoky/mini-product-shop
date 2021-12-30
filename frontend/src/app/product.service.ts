import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';
import { Product } from './product';

@Injectable({
  providedIn: 'root'
})
export class ProductService {
  constructor(private http: HttpClient) { }

  getItems() : Observable<Product[]> {
    return this.http.get<Product[]>("http://127.0.0.1:8000/products");
  }

  getItem(id: number) : Observable<Product> {
    return this.http.get<Product>("http://127.0.0.1:8000/products/" + id);
  }
}
