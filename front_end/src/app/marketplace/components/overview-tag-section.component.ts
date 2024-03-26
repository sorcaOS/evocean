import { Component, OnInit } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import { CommonModule } from '@angular/common';
import { Product } from '../../interfaces/product';
import { ProductService } from '../../services/product.service';

@Component({
  selector: 'evocean-overview-tag-section',
  standalone: true,
  imports: [CommonModule],
  templateUrl: './overview-tag-section.component.html',
  styleUrl: './overview-tag-section.component.css'
})
export class OverviewTagSectionComponent implements OnInit {
  private productID: string | null = null;
  product: Product | undefined;

  constructor(private productService: ProductService, private route: ActivatedRoute) {
  }

  ngOnInit(): void {
    this.product = this.productService.selectedProduct;
  }
}