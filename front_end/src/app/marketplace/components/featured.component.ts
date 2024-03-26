import { Component, OnInit } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Product } from '../../interfaces/product';
import { interval } from 'rxjs';
import { startWith, switchMap } from 'rxjs/operators';
import { CommonModule } from '@angular/common';
import { FeaturedItemComponent } from './featured-item.component';
import { ProductService } from '../../services/product.service';
import { CurrencyRateService } from '../../services/currency-rate.service';

@Component({
  selector: 'evocean-featured',
  standalone: true,
  imports: [CommonModule, FeaturedItemComponent],
  templateUrl: './featured.component.html',
  styleUrl: './featured.component.css'
})
export class FeaturedComponent implements OnInit {
  items: Product[] = [];

  constructor(private http: HttpClient, private currencyRateService: CurrencyRateService,
              private productService: ProductService
  ) {
  }

  ngOnInit(): void {
    this.fetchRealtimeUSDPrice();
    this.productService.get_list({ 'is_featured': true }).subscribe((resp) => {
      console.log(resp);
      this.items = resp.results;
    });


  }

  fetchRealtimeUSDPrice(): void {
    // query API every 60 seconds
    interval(60000)
      .pipe(
        startWith(0),
        switchMap(() => this.currencyRateService.getCurrencyRate('solana'))
      )
      .subscribe((resp) => {
        console.log(resp);
        this.items.forEach(item => {
          item.price_usd = item.price * resp.price;
        });
      });
  }
}