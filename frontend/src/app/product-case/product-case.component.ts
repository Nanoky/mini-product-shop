import { Component, Input, OnInit } from '@angular/core';
import { Product } from '../product';

@Component({
  selector: 'app-product-case',
  templateUrl: './product-case.component.html',
  styleUrls: ['./product-case.component.scss']
})
export class ProductCaseComponent implements OnInit {

  @Input() product: Product | undefined;

  constructor() { }

  ngOnInit(): void {

  }

}
