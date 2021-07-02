import { Component, Input, OnInit } from '@angular/core';
import { NgbActiveModal } from '@ng-bootstrap/ng-bootstrap';
import { Product } from 'src/app/models/product.model';
import { ProductService } from 'src/app/services/product.service';
import { ToastService } from 'src/app/services/toast.service';

@Component({
  selector: 'app-add-product',
  templateUrl: './add-product.component.html',
  styleUrls: ['./add-product.component.css']
})
export class AddProductComponent implements OnInit {

  product: Product = new Product()

  constructor(private productService: ProductService,
    public activeModal: NgbActiveModal,
    private toastService: ToastService) { }

  ngOnInit(): void {

  }

  postProduct() {
    if (!this.product.image) {
      this.toastService.show("Please add an image", { classnmae: 'bg-danger text-light', delay: 5000 })
      return
    }
    this.productService.post(this.product).subscribe(result => {
      this.toastService.show("Product added", { classnmae: 'bg-success text-light', delay: 5000 })
      this.activeModal.close()
    })
  }

  imageUploaded(imageId: string) {
    this.product.image = imageId
  }

}
