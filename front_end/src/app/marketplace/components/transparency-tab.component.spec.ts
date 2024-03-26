import { ComponentFixture, TestBed } from '@angular/core/testing';
import { TransparencyTabComponent } from './transparency-tab.component';

describe('DetailTagSectionComponent', () => {
  let component: TransparencyTabComponent;
  let fixture: ComponentFixture<TransparencyTabComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [TransparencyTabComponent],
    }).compileComponents();

    fixture = TestBed.createComponent(TransparencyTabComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
