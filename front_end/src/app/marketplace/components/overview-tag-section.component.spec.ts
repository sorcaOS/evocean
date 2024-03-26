import { ComponentFixture, TestBed } from '@angular/core/testing';
import { OverviewTagSectionComponent } from './overview-tag-section.component';

describe('OverviewTagSectionComponent', () => {
  let component: OverviewTagSectionComponent;
  let fixture: ComponentFixture<OverviewTagSectionComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [OverviewTagSectionComponent],
    }).compileComponents();

    fixture = TestBed.createComponent(OverviewTagSectionComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
