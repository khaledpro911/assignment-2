// ILLUSTRATIVE — syntax verified, not executed in CI
import { Controller, Get } from "@nestjs/common";
@Controller("status")
export class StatusController {
  @Get() read() { return { ok: true }; }
}
