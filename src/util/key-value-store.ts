import { type Boss } from '../boss'
import { BoolArraySerializer } from './bool-array-serializer'

export class KeyValueStorage {
  private static apiUrl = 'https://keyvalue.immanuel.co/api/KeyVal'
  private static bossesKey = 'bosses-defeated'
  private static noneDefeated = '~'

  private apiKey: string

  public constructor(apiKey: string) {
    this.apiKey = apiKey
  }

  public async saveBossesDefeated(bosses: Boss[]) {
    const defeatedArray = bosses.map((boss) => boss.defeated)
    const defeatedBase64 = BoolArraySerializer.toBase64String(defeatedArray)
    await this.writeValue(KeyValueStorage.bossesKey, defeatedBase64)
  }

  public async loadBossesDefeated(bosses: Boss[]) {
    const defeatedBase64 = await this.getValue(KeyValueStorage.bossesKey)
    if (defeatedBase64 !== undefined && defeatedBase64 !== KeyValueStorage.noneDefeated) {
      const defeatedArray = BoolArraySerializer.fromBase64String(defeatedBase64)
      for (let i = 0; i < bosses.length && i < defeatedArray.length; i++) {
        bosses[i].defeated = defeatedArray[i]
      }
    }
  }

  public async clearBossesDefeated() {
    await this.writeValue(KeyValueStorage.bossesKey, KeyValueStorage.noneDefeated)
  }

  private async writeValue(key: string, value: string) {
    const response = await fetch(
      `${KeyValueStorage.apiUrl}/UpdateValue/${this.apiKey}/${key}/${value}`,
      {
        method: 'POST',
      },
    )
    if (!response.ok) {
      console.error(response)
    }
  }

  private async getValue(key: string) {
    const response = await fetch(`${KeyValueStorage.apiUrl}/GetValue/${this.apiKey}/${key}`, {
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
