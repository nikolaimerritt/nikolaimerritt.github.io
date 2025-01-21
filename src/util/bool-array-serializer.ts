export class BoolArraySerializer {
  private static _base64Chars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789-_'
  private static _groupSize = 6

  public static toBase64String(boolArray: boolean[]): string {
    const boolGroups = BoolArraySerializer.boolArrayToBoolGroups(boolArray)
    const chars: string[] = []
    for (const group of boolGroups) {
      const int = BoolArraySerializer.boolGroupToInt(group)
      chars.push(BoolArraySerializer._base64Chars[int])
    }
    return chars.join('')
  }

  public static fromBase64String(base64: string): boolean[] {
    const boolGroups = []
    for (let i = 0; i < base64.length; i++) {
      const int = this._base64Chars.indexOf(base64[i])
      boolGroups.push(BoolArraySerializer.intToBoolGroup(int))
    }
    return boolGroups.flat()
  }

  private static boolArrayToBoolGroups(boolArray: boolean[]): boolean[][] {
    const boolGroups = []
    for (let i = 0; i < boolArray.length; i += BoolArraySerializer._groupSize) {
      const group = boolArray.slice(i, i + BoolArraySerializer._groupSize)
      while (group.length < BoolArraySerializer._groupSize) {
        group.push(false)
      }
      boolGroups.push(group)
    }
    return boolGroups
  }

  private static boolGroupToInt(boolGroup: boolean[]): number {
    let int = 0
    for (let i = 0; i < boolGroup.length; i++) {
      if (boolGroup[i]) {
        const powerOfTwo = 1 << i
        int |= powerOfTwo
      }
    }
    return int
  }

  private static intToBoolGroup(int: number): boolean[] {
    const boolGroup = []
    for (let i = 0; i < BoolArraySerializer._groupSize; i++) {
      const bit = 1 << i
      boolGroup.push(Boolean(int & bit))
    }
    return boolGroup
  }
}
