import { ChangeDetectorRef, Component, OnInit } from '@angular/core';
import { RouterModule } from '@angular/router';
import { EnvironmentService, FirebaseModule } from '@omelet/shared-components';
import { HttpClientModule } from '@angular/common/http';
import { MatToolbar } from '@angular/material/toolbar';
import { NgIf } from '@angular/common';
import { LayoutService } from '../../../chat/src/app/services/layout.service';
import { HeaderComponent } from './components/header.component';
import { FooterComponent } from './components/footer.component';
import { CurrencyRateService } from './services/currency-rate.service';
import { environment } from '../environments/environment';

@Component({
  standalone: true,
  imports: [RouterModule, FirebaseModule, HttpClientModule, MatToolbar, NgIf, HeaderComponent, FooterComponent],
  selector: 'omelet-root',
  templateUrl: './app.component.html',
  styleUrl: './app.component.scss'
})
export class AppComponent implements OnInit {
  title = 'evocean';
  protected headerVisible = true;

  constructor(protected layoutService: LayoutService, protected changeDetector: ChangeDetectorRef, private environmentService: EnvironmentService,
              private currencyRateService: CurrencyRateService
  ) {
    this.environmentService.setApiUrl(environment.api_url);
    console.log('version 0.0.1');
  }

  ngOnInit(): void {
    this.layoutService.headerVisible.subscribe(visible => {
      this.headerVisible = visible;
      this.changeDetector.detectChanges();
    });
    this.currencyRateService.getCurrencyRate('solana').subscribe((resp) => {
      console.log(resp.price_unit, '=', resp.price, ' $');
    });
  }

}
