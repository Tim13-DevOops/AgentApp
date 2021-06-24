
import { ProductIdQuantity } from "./productId-quantity";


export class Order {
    user_name: string;
    user_surname: string;
    user_email: string;
    user_address: string;
    user_phone_number: string;
    products: ProductIdQuantity[];

    constructor(obj?: any) {
        this.user_name = obj && obj.user_name || "";
        this.user_surname = obj && obj.user_surname || "";
        this.user_email = obj && obj.user_email || "";
        this.user_address = obj && obj.user_address || "";
        this.user_phone_number = obj && obj.user_phone_number || "";
        this.products = obj && obj.products
            && obj.products.map((x: any) => new ProductIdQuantity(x)) || [];
    }
}