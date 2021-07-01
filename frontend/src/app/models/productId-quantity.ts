import { Product } from "./product.model";

export class ProductIdQuantity {
    product_id: number
    quantity: number;

    constructor(obj?: any) {
        this.product_id = obj && obj.product_id || null;
        this.quantity = obj && obj.quantity || 0;
    }
}