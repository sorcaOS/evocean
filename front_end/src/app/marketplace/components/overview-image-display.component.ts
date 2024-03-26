import { Component, Input } from '@angular/core';
import { CommonModule } from '@angular/common';

@Component({
  selector: 'evocean-overview-image-display',
  standalone: true,
  imports: [CommonModule],
  templateUrl: './overview-image-display.component.html',
  styleUrl: './overview-image-display.component.css',
})
export class OverviewImageDisplayComponent {
  @Input() mainImageUrl!: string;
}
