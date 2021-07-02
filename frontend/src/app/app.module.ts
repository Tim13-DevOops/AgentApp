import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { HomeComponent } from './components/core/home/home.component';
import { HttpClientModule } from '@angular/common/http';
import { ProductsComponent } from './components/products/products.component';
import { ProductComponent } from './components/products/product/product.component';
import { NavBarComponent } from './components/core/nav-bar/nav-bar.component';
import { NgbModule } from '@ng-bootstrap/ng-bootstrap';
import { AddProductComponent } from './components/products/add-product/add-product.component';
import { UpdateProductComponent } from './components/products/update-product/update-product.component';
import { FormsModule } from '@angular/forms';
import { ProductPageComponent } from './components/products/product-page/product-page.component';
import { CartComponent } from './components/order/cart/cart.component';
import { OrderComponent } from './components/order/order.component';
import { ToastGlobalComponent } from './components/core/toast/toast-global/toast-global.component';
import { ToastContainer } from './components/core/toast/toast-container/toast-container.component';
import { ImageUploadComponent } from './components/products/add-product/image-upload/image-upload.component';

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
    OrderComponent,
    ToastGlobalComponent,
    ToastContainer,
    ImageUploadComponent,
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    HttpClientModule,
    NgbModule,
    FormsModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
