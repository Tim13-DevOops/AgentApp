import { Component, Input, OnInit } from '@angular/core';
import { NgbActiveModal } from '@ng-bootstrap/ng-bootstrap';
import { Product } from 'src/app/models/product.model';
import { ProductService } from 'src/app/services/product.service';
import { ToastService } from 'src/app/services/toast.service';

@Component({
  selector: 'app-update-product',
  templateUrl: './update-product.component.html',
  styleUrls: ['./update-product.component.css']
})
export class UpdateProductComponent implements OnInit {

  @Input()
  product: Product

  constructor(private productService: ProductService,
    public activeModal: NgbActiveModal,
    private toastService: ToastService) { }

  ngOnInit(): void {
  }

  putProduct() {
    this.productService.put(this.product).subscribe(result => {
      this.activeModal.close()
    }, err => {
      this.toastService.show(`${err.code} ${err.message}`, { classname: 'bg-danger text-light', delay: 5000 })
    })
  }

}
