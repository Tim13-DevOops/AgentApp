import { Component, EventEmitter, Input, OnInit, Output } from '@angular/core';
import { NgbModal } from '@ng-bootstrap/ng-bootstrap';
import { Product } from 'src/app/models/product-model';
import { ProductService } from 'src/app/services/product.service';
import { UpdateProductComponent } from '../update-product/update-product.component';

@Component({
  selector: 'app-product',
  templateUrl: './product.component.html',
  styleUrls: ['./product.component.css']
})
export class ProductComponent implements OnInit {

  @Input()
  product: Product

  @Output()
  productsChanged = new EventEmitter<boolean>()
  
  constructor(private modalService: NgbModal, private productService: ProductService) { }

  ngOnInit(): void {
  }

  openEditDialog() {
    let modalRef = this.modalService.open(UpdateProductComponent)
    modalRef.componentInstance.product = new Product(this.product)
    modalRef.closed.subscribe(() => {
      this.productsChanged.emit(true)
    })
  }

  deleteProduct() {
    this.productService.delete(this.product.id).subscribe(result => {
      this.productsChanged.emit(true)
    })
  }

}
