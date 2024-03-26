import { AfterContentInit, Component, OnInit } from '@angular/core';
import { ActivatedRoute, RouterLink, RouterOutlet } from '@angular/router'; // Import ActivatedRoute to access the route parameters.
import { CommonModule } from '@angular/common';
import { ProductService } from '../services/product.service';
import { Product } from '../interfaces/product';
import { HumanNumberPipe } from '@omelet/shared-components';
import { MatIcon } from '@angular/material/icon';
import { ProductCardComponent } from './components/product-card.component';

@Component({
  selector: 'evocean-product-overview',
  standalone: true,
  imports: [CommonModule, HumanNumberPipe, MatIcon, RouterOutlet, RouterLink, ProductCardComponent],
  templateUrl: './product-overview.component.html',
  styleUrl: './product-overview.component.css'
})
export class ProductOverviewComponent implements OnInit, AfterContentInit {
  selectedImage: string = 'https://via.placeholder.com/658x475';
  product!: Product;
  productId!: string | null; // Declare a variable to hold the product Id.
  images: string[] = [];
  suggestionProducts: Product[] = [];

  sectionTabs = [{ title: 'Overview', route: 'overview', isActive: true }, {
    title: 'Details',
    route: 'details',
    isActive: false
  }, { title: 'Reviews', route: 'reviews', isActive: false }];

  constructor(private productService: ProductService, private route: ActivatedRoute) { // Inject ActivatedRoute in the constructor.
  }

  ngAfterContentInit(): void {
    this.productService.get_list({'page_size':4}).subscribe(products => {
      this.suggestionProducts = products.results;
    });
  }

  ngOnInit(): void {
    this.productId = this.route.snapshot.paramMap.get('id') ?? '1';
    this.productService.get(this.productId).subscribe(product => { // Fetch the product details using the product Id.
      this.product = product;
      this.productService.selectedProduct = product;
      this.selectedImage = product.thumbnail_image.image;
      this.product.preview_images.forEach(image => {
        this.images.push(image.image);
      });
    });
  }

  onTabClick(tab: any) {
    this.sectionTabs.forEach(sectionTab => {
      sectionTab.isActive = false;
    });

    tab.isActive = true;

  }

  onSuggestionsClick(suggestionProduct: Product) {
      window.location.href = `/marketplace/product/${suggestionProduct.id}`;
  }
}