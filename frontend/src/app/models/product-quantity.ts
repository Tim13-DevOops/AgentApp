import { Product } from "./product-model";

export class ProductQuantity {
    product: Product
    quantity: number;

    constructor(obj?:any) {
        this.product = obj && obj.product || new Product();
        this.quantity = obj && obj.availability || 0;
    }
}