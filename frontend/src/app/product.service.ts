import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';
import { Page } from './Page';
import { Product } from './product';

@Injectable({
  providedIn: 'root'
})
export class ProductService {
  constructor(private http: HttpClient) { }

  getItems(page: number = 1, size: number = 50) : Observable<Page> {
    return this.http.get<Page>("http://127.0.0.1:8000/products?page=" + page + "&size=" + size);
  }

  getItem(id: number) : Observable<Product> {
    return this.http.get<Product>("http://127.0.0.1:8000/products/" + id);
  }
}
