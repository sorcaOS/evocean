import { Injectable } from '@angular/core';
import { AbstractService } from '@omelet/shared-components';
import { CurrencyRate } from '../interfaces/currency-rate';
import { map } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class CurrencyRateService extends AbstractService<CurrencyRate> {
  override end_point = '/price';

  public getCurrencyRate(currency: string) {
    return this.get<CurrencyRate>(currency).pipe(
      map((response) => {
        // save to local storage
        localStorage.setItem('sol_rate', response.price.toString());
        return response;
      })
    );
  }
}
