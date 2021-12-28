import { ComponentFixture, TestBed } from '@angular/core/testing';

import { ProductCaseComponent } from './product-case.component';

describe('ProductCaseComponent', () => {
  let component: ProductCaseComponent;
  let fixture: ComponentFixture<ProductCaseComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ ProductCaseComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(ProductCaseComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
