import { Route } from '@angular/router';
import { MarketplaceComponent } from './marketplace/marketplace.component';
import { ProductOverviewComponent } from './marketplace/product-overview.component';
import { OverviewTagSectionComponent } from './marketplace/components/overview-tag-section.component';
import { TransparencyTabComponent } from './marketplace/components/transparency-tab.component';
import { OwnerBiddingTabComponent } from './marketplace/components/owner-bidding-tab.component';

export const appRoutes: Route[] = [
  { path: '', redirectTo: '/marketplace', pathMatch: 'full' },
  { path: 'auth', loadChildren: () => import('@omelet/shared-components').then(m => m.AuthModule) },
  {
    path: 'marketplace',
    component: MarketplaceComponent
    // canActivate: [isAuthenticatedGuard],
    // runGuardsAndResolvers: 'always',
    // children: [{ path: ':id', component: MainChatComponent }],
  },
  {
    path: 'marketplace/product/:id',
    component: ProductOverviewComponent,
    children: [
      { path: 'overview', component: OverviewTagSectionComponent },
      { path: 'details', component: TransparencyTabComponent },
      { path: 'reviews', component: OwnerBiddingTabComponent },
      { path: '', redirectTo: 'overview', pathMatch: 'full' }
    ]
  }
];