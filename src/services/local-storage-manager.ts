export class LocalStorageManager {
    private readonly shouldShowWizardKey = "wizard";

    public shouldShowWizard(): boolean {
        const storedValue = this._get(this.shouldShowWizardKey);
        return storedValue === "true";
    }

    public setShowWizard(show: boolean): void {
        this._set(this.shouldShowWizardKey, show.toString());
    }

    private _get(key: string): string {
        return localStorage.getItem(key);
    }

    private _set(key: string, value: string): void {
        localStorage.setItem(key, value);
    }
    
}