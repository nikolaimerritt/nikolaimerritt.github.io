import type { Boss, Area } from "@/areas";

export class BossesApi {
    private static apiUrl = "https://elden-ring.click/api"
    private password: string

    public constructor(password: string) {
        this.password = password
    }

    private authHeaders(): HeadersInit {
        return { "UserID": this.password }
    }

    public static async getPassword(): Promise<string> {
        const response = await fetch(`${BossesApi.apiUrl}/signup`, {
            method: "POST",
        });
        if (response.ok) {
            return JSON.parse(await response.text()).id;
        } else {
            console.error(response);
            throw new Error(await response.text());
        }
    }

    public async saveBossDefeated(boss: Boss) {
        const response = await fetch(`${BossesApi.apiUrl}/boss/${boss.id}/defeated/${boss.defeated}`, {
            method: "POST",
            headers: this.authHeaders()
        });
        if (!response.ok) {
            console.error(response);
            throw new Error(await response.text());
        }
    }

    public async getAreas(): Promise<Area[]> {
        const response = await fetch(`${BossesApi.apiUrl}/areas`, {
            method: "GET",
            headers: this.authHeaders()
        });
        if (response.ok) {
            return JSON.parse(await response.text());
        } else {
            console.error(response);
            throw new Error(await response.text())
        }
    }
}