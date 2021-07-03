import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { HomeComponent } from './components/core/home/home.component';
import { ProductPageComponent } from './components/products/product-page/product-page.component';
import { ProductsComponent } from './components/products/products.component';
import { OrderComponent } from './components/order/order.component';
import { LoginComponent } from './components/core/login/login.component';

const routes: Routes = [
  { path: "home", component: HomeComponent },
  { path: "login", component: LoginComponent },
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
