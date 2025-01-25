import type { Area } from '@/areas'
import { BoolArraySerializer } from './bool-array-serializer'

export class KeyValueStorage {
  private static apiUrl = 'https://keyvalue.immanuel.co/api/KeyVal'
  private static bossesKey = 'bosses-defeated'
  private static noneDefeated = '~'

  private password: string

  public constructor(password: string) {
    this.password = password
  }

  public static async getPassword(): Promise<string> {
    const response = await fetch(`${KeyValueStorage.apiUrl}/GetAppKey`, {
      method: 'GET',
    })
    if (response.ok) {
      return (await response.text()).trim().replace(/\"/g, '')
    } else {
      console.error(response)
      throw new Error(await response.text())
    }
  }

  public async saveBossesDefeated(areas: Area[]) {
    const defeatedArray = areas.flatMap((area) => area.bosses).map((boss) => boss.defeated)
    const defeatedBase64 = BoolArraySerializer.toBase64String(defeatedArray)
    await this.writeValue(KeyValueStorage.bossesKey, defeatedBase64)
  }

  public async loadBossesDefeated(area: Area[]): Promise<Area[]> {
    const areasClone = structuredClone(area)
    const defeatedBase64 = await this.getValue(KeyValueStorage.bossesKey)
    if (defeatedBase64 !== undefined && defeatedBase64 !== KeyValueStorage.noneDefeated) {
      const defeatedArray = BoolArraySerializer.fromBase64String(defeatedBase64)
      // TO SELF: this doesnt work if flatmap does a deep copy, but I dont think flatmap does
      const bosses = areasClone.flatMap((area) => area.bosses)
      for (let i = 0; i < bosses.length && i < defeatedArray.length; i++) {
        bosses[i].defeated = defeatedArray[i]
      }
    }
    return areasClone
  }

  public async clearBossesDefeated() {
    await this.writeValue(KeyValueStorage.bossesKey, KeyValueStorage.noneDefeated)
  }

  private async writeValue(key: string, value: string) {
    const response = await fetch(
      `${KeyValueStorage.apiUrl}/UpdateValue/${this.password}/${key}/${value}`,
      {
        method: 'POST',
      },
    )
    if (!response.ok) {
      console.error(response)
    }
  }

  private async getValue(key: string) {
    const response = await fetch(`${KeyValueStorage.apiUrl}/GetValue/${this.password}/${key}`, {
      method: 'GET',
    })
    if (response.ok) {
      return (await response.text()).trim().replace(/"/g, '')
    } else {
      console.error(response)
      return undefined
    }
  }
}
