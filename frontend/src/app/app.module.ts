import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { HomeComponent } from './core/home/home.component';
import { HttpClientModule } from '@angular/common/http';
import { ProductsComponent } from './products/products.component';
import { ProductComponent } from './products/product/product.component';
import { NavBarComponent } from './core/nav-bar/nav-bar.component';
import { NgbModule } from '@ng-bootstrap/ng-bootstrap';
import { AddProductComponent } from './products/add-product/add-product.component';
import { UpdateProductComponent } from './products/update-product/update-product.component';
import { FormsModule } from '@angular/forms';
import { ProductPageComponent } from './products/product-page/product-page.component';
import { CartComponent } from './order/cart/cart.component';
import { OrderComponent } from './order/order.component';

@NgModule({
  declarations: [
    AppComponent,
    HomeComponent,
    ProductsComponent,
    ProductComponent,
    NavBarComponent,
    AddProductComponent,
    UpdateProductComponent,
    ProductPageComponent,
    CartComponent,
    OrderComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    HttpClientModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
