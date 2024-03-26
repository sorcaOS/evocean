import { Injectable } from '@angular/core';
import { AbstractService } from '@omelet/shared-components';
import { Product } from '../interfaces/product';
import { map, Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class ProductService extends AbstractService<Product> {
  override end_point = '/products';
  selectedProduct: Product | undefined;

  // @ts-ignore
  override get_list(params?: any): Observable<{
    count: number;
    next: string | null;
    previous: string | null;
    results: Product[]
  }> {
    const sol_rate_str = localStorage.getItem('sol_rate') || '1';
    const sol_rate = parseFloat(sol_rate_str);
    return super.get_list(params).pipe(
      map((response) => {
        response.results.map(
          (product) => {
            console.log('Product price in USD:', product.price_usd);
            product.price_usd = product.price * sol_rate;
            return product;
          }
        );
        return response;
      })
    );
  }

  // @ts-ignore
  override get(id: string): Observable<Product> {
    return super.get(id).pipe(
      map((product) => {
        console.log('Product price in USD:', product.price_usd);
        const sol_rate_str = localStorage.getItem('sol_rate') || '1';
        const sol_rate = parseFloat(sol_rate_str);
        product.price_usd = product.price * sol_rate;
        return product;
      })
    );
  }
}
