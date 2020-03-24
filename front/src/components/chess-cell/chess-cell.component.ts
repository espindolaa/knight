import { Component, OnInit, Input, EventEmitter, Output } from '@angular/core';
import { AlgebraicPosition } from 'src/model/algebraic-position';
import { Observable, BehaviorSubject } from 'rxjs';

@Component({
  selector: 'app-chess-cell',
  templateUrl: './chess-cell.component.html',
  styleUrls: ['./chess-cell.component.scss']
})
export class ChessCellComponent implements OnInit {

  @Input() position: AlgebraicPosition;
  @Input() knightPosition$: Observable<AlgebraicPosition>;
  @Input() highlightedPositions$: Observable<AlgebraicPosition[]>;

  @Output() cellClicked = new EventEmitter<AlgebraicPosition>();

  public isKnight$ = new BehaviorSubject<boolean>(false);
  public isHighlighted$ = new BehaviorSubject<boolean>(false);

  constructor() {
   }

  ngOnInit(): void {
    this.knightPosition$.subscribe(k => this.isKnight$.next(k === this.position));
    this.highlightedPositions$.subscribe(h => this.isHighlighted$.next(h.includes(this.position)));
  }

  public click() {
    this.cellClicked.emit(this.position);
  }

  public isOddCell() {
    return (this.position.column.charCodeAt(0) + this.position.row) % 2 === 1;
  }

}
