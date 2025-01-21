export class CookieManager {
  private static tokenCookieName = 'token'
  private static tokenCookieExpirationDays = 365

  public static getTokenCookie(): string | undefined {
    const token = CookieManager.getCookie(CookieManager.tokenCookieName)
    // Refreshing cookie
    if (token !== undefined) {
      CookieManager.setTokenCookie(token)
    }
    return token
  }

  public static setTokenCookie(token: string) {
    CookieManager.setCookie(
      CookieManager.tokenCookieName,
      token,
      CookieManager.tokenCookieExpirationDays,
    )
  }

  public static deleteTokenCookie() {
    CookieManager.deleteCookie(CookieManager.tokenCookieName)
  }

  private static setCookie(cookieKey: string, cookieValue: string, expirationDays: number) {
    let expiryDate = ''
    if (expirationDays) {
      const date = new Date()
      date.setTime(
        Number.parseInt(`${date.getTime()}${expirationDays || 30 * 24 * 60 * 60 * 1000}`),
      )
      expiryDate = `; expires=${date.toUTCString()}`
    }
    document.cookie = `${cookieKey}=${cookieValue || ''}${expiryDate}; path=/; samesite=Lax; secure`
  }

  private static deleteCookie(cookieKey: string) {
    const unixEpoch = new Date(0)
    document.cookie = `${cookieKey}=none;path=/;expires=${unixEpoch.toUTCString()}`
  }

  private static getCookie(cookieKey: string): string | undefined {
    const cookieName = `${cookieKey}=`
    const cookieArray = document.cookie.split(';')
    for (let cookie of cookieArray) {
      while (cookie.charAt(0) == ' ') {
        cookie = cookie.substring(1, cookie.length)
      }

      if (cookie.indexOf(cookieName) == 0) {
        return cookie.substring(cookieName.length, cookie.length)
      }
    }
    return undefined
  }
}
