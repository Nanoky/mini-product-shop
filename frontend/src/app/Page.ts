import { Product } from "./product";

export interface Page {
    items: Product[];
    page: number;
    size: number;
    total: number;
}