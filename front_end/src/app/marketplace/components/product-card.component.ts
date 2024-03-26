import { Component, Input } from '@angular/core';
import { CommonModule } from '@angular/common';
import { Product } from '../../interfaces/product';
import { HumanNumberPipe, MaxTextLengthPipe } from '@omelet/shared-components';

@Component({
  selector: 'evocean-product-card',
  standalone: true,
  imports: [CommonModule, HumanNumberPipe, MaxTextLengthPipe],
  templateUrl: './product-card.component.html',
  styleUrl: './product-card.component.css'
})
export class ProductCardComponent {
  @Input() product!: Product;
}
