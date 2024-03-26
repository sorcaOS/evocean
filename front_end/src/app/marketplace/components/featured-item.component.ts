import { Component, Input } from '@angular/core';
import { CommonModule } from '@angular/common';
import { Product } from '../../interfaces/product';
import { HumanNumberPipe, MaxTextLengthPipe } from '@omelet/shared-components';

@Component({
  selector: 'evocean-featured-item',
  standalone: true,
  imports: [CommonModule, HumanNumberPipe, MaxTextLengthPipe],
  templateUrl: './featured-item.component.html',
  styleUrl: './featured-item.component.css',
})
export class FeaturedItemComponent {
  @Input() item!: Product;
}
