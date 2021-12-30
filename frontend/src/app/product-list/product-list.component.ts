import { Component, OnInit } from '@angular/core';
import { PageEvent } from '@angular/material/paginator';
import { Observable } from 'rxjs';
import { Page } from '../Page';
import { Product } from '../product';
import { ProductService } from '../product.service';

@Component({
  selector: 'app-product-list',
  templateUrl: './product-list.component.html',
  styleUrls: ['./product-list.component.scss']
})
export class ProductListComponent implements OnInit {

  pages: Page | undefined;
  products: Product[] = [];
  page: number = 0;
  size: number = 10;

  constructor(private service: ProductService) { 
    
  }

  ngOnInit(): void {
    this.loadData()
  }

  loadData() {
    this.service.getItems(this.page + 1, this.size).subscribe((data: Page) => {
      this.pages = data;
      this.products = this.pages.items;
      this.size = this.pages.size;
      this.page = this.pages.page - 1;
    });
  }

  handlePage(event: PageEvent) {
    this.page = event.pageIndex;
    this.size = event.pageSize;
    this.loadData();
  }

}
