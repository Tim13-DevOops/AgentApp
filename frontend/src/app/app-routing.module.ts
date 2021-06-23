import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { HomeComponent } from './core/home/home.component';
import { ProductPageComponent } from './products/product-page/product-page.component';
import { ProductsComponent } from './products/products.component';
import { OrderComponent } from './order/order.component';

const routes: Routes = [
  { path: "home", component: HomeComponent },
  { path: "products", component: ProductsComponent },
  { path: "cart", component: OrderComponent },
  { path: "product/:product_id", component: ProductPageComponent },
  { path: "", redirectTo: "/home", pathMatch: "full" },
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
