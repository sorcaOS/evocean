import { ComponentFixture, TestBed } from '@angular/core/testing';
import { OverviewImageDisplayComponent } from './overview-image-display.component';

describe('OverviewImageDisplayComponent', () => {
  let component: OverviewImageDisplayComponent;
  let fixture: ComponentFixture<OverviewImageDisplayComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [OverviewImageDisplayComponent],
    }).compileComponents();

    fixture = TestBed.createComponent(OverviewImageDisplayComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
