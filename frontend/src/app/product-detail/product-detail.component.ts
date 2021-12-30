import { Component, OnInit } from '@angular/core';
import { MatSnackBar, MatSnackBarConfig, MAT_SNACK_BAR_DEFAULT_OPTIONS } from '@angular/material/snack-bar';
import { ActivatedRoute, Router } from '@angular/router';
import { GlobalComponent } from '../global-component';
import { Product } from '../product';
import { ProductService } from '../product.service';

@Component({
  selector: 'app-product-detail',
  templateUrl: './product-detail.component.html',
  styleUrls: ['./product-detail.component.scss']
})
export class ProductDetailComponent implements OnInit {

  product: Product | undefined;
  currency = GlobalComponent.currenty;

  constructor(private route: ActivatedRoute, private service: ProductService, private snackbar: MatSnackBar, private router: Router) { }

  ngOnInit(): void {
    const productId = Number(this.route.snapshot.paramMap.get('id'));
    this.service.getItem(productId).subscribe((data : Product) => this.product = data);
  }

  checkout() {
    this.snackbar.open("Thank you for buying " + this.product?.name, "Close", {
      verticalPosition: 'top'
    });
  }

  backToList() {
    this.snackbar.open("Thank you shopping with us", "Close", {
      duration: 5000,
      verticalPosition: 'top'
    });
    this.router.navigateByUrl("/products");
  }

}
