import { Component, Input, OnInit } from '@angular/core';
import { NgbActiveModal } from '@ng-bootstrap/ng-bootstrap';
import { Product } from 'src/app/models/product-model';
import { ProductService } from 'src/app/services/product.service';

@Component({
  selector: 'app-add-product',
  templateUrl: './add-product.component.html',
  styleUrls: ['./add-product.component.css']
})
export class AddProductComponent implements OnInit {

  product: Product = new Product()

  constructor(private productService: ProductService,
              public activeModal: NgbActiveModal) { }

  ngOnInit(): void {

  }

  postProduct() {
    this.productService.post(this.product).subscribe(result => {
      this.activeModal.close()
    })
  }

}
