import { AlgebraicPosition } from 'src/model/algebraic-position';
import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable, BehaviorSubject } from 'rxjs';

@Injectable()
export class ChessService {
    
    constructor(private http: HttpClient) { }

    private _positions$ = new BehaviorSubject<AlgebraicPosition[]>([]);
    public positions$ = this._positions$.asObservable();

    public getPossibleMoves(startingPosition: AlgebraicPosition): Observable<AlgebraicPosition[]> {
        const request = this.http.get(`http://localhost:5000/api/v1/possibleMoves/${startingPosition.column}${startingPosition.row}`);
        request.subscribe(v => this._positions$.next(this.mapToAlgebraic(v)));
        return this.positions$;
    }

    private mapToAlgebraic(algebraicArray): AlgebraicPosition[] {
        const positions: AlgebraicPosition[] = [];
        algebraicArray.forEach(element => {
            positions.push(new AlgebraicPosition(element[0], element[1]));
        });
        return positions;
    }
    
}