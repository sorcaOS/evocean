import { Component, OnInit } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FeaturedComponent } from './components/featured.component';
import { Product } from '../interfaces/product';
import { ProductService } from '../services/product.service';
import { HumanNumberPipe, MaxTextLengthPipe } from '@omelet/shared-components';
import { ProductCardComponent } from './components/product-card.component';
import { RouterLink } from '@angular/router';

@Component({
  selector: 'omelet-marketplace',
  standalone: true,
  imports: [CommonModule, FeaturedComponent, MaxTextLengthPipe, HumanNumberPipe, ProductCardComponent, RouterLink],
  templateUrl: './marketplace.component.html',
  styleUrl: './marketplace.component.scss'
})
export class MarketplaceComponent implements OnInit{
  badges: string[] = ['UI Kit', 'Template', 'Framer', 'Webflow', 'Badge'];

  features = [{
    title: 'Discover top-tier curated products.',
    description: 'Our marketplace ensures excellence through rigorous selection.',
    image: 'assets/images/feature1.svg'
  }, {
    title: 'Blockchain-powered transparency',
    description: 'Track product history and transactions for trust and clarity.',
    image: 'assets/images/feature2.svg'
  }, {
    title: 'Value for all',
    description: 'Earn rewards, access exclusive deals, and enjoy secure transactions on our platform.',
    image: 'assets/images/feature3.svg'
  }];
  products: Product[] = []

  constructor(private productService: ProductService) {
  }

  ngOnInit() {
    this.productService.get_list().subscribe((products) => {
      this.products = products.results
    });
  }
}