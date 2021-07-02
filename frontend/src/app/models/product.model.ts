

export class Product {
    id: number;
    timestamp: string;
    name: string;
    price: number;
    availability: number;
    image: string;

    constructor(obj?: any) {
        this.id = obj && obj.id || null;
        this.timestamp = obj && obj.timestamp || '';
        this.name = obj && obj.name || '';
        this.price = obj && obj.price || '';
        this.availability = obj && obj.availability || 0;
        this.image = obj && obj.image || '';
    }
}